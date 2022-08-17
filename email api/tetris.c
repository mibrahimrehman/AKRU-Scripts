/*
 * ATTENZIONE !!!
 * Ci possono essere moltissime soluzioni allo stesso esercizio.
 * Questa non è "la" soluzione corretta.
 * Anzi, potrebbero esserci degli errori, sta a voi trovarli !
 *
 * es: al momento non viene gestito il caso in cui l'utente prova a inserire una pedina in una colonna piena
 *
 * buon lavoro!
 */

#include <stdio.h>
#include <stdlib.h>

/* Casella del piano di gioco */
enum casella {VUOTO, PLAYER_1, PLAYER_2};
typedef enum casella casella_t;

/* Piano di gioco */
/* nota: piano_t è un puntatore */
typedef casella_t *piano_t;

typedef enum bool {FALSE, TRUE} bool_t;

void init(piano_t piano, int ROWS, int COLS) {
    int r, c;
    for (r=0; r<ROWS; r++) {
        for (c=0; c<COLS; c++) {
            piano[r*COLS + c] = VUOTO;
        }
    }
}

casella_t prossimo_turno (casella_t turno) {
    if (turno == PLAYER_1)
        return PLAYER_2;
    else
        return PLAYER_1;
}

void stampa(piano_t piano, int ROWS, int COLS) {
    int r, c;
    for (r=0; r<ROWS; r++) {
        for (c=0; c<COLS; c++) {
            casella_t casella = piano[r*COLS + c];
            if (casella==VUOTO)
                printf("_");
            else if (casella==PLAYER_1)
                printf("X");
            else
                printf("O");
        }
        printf("\n");
    }
    for (c=0; c<COLS; c++)
        printf("%d", c);
    printf("\n");
}

int mossa(piano_t piano, int ROWS, int COLS,
          int mossa_c, casella_t player) {
    int r, c;
    for(r=ROWS-1; r>=0; r--) {
        casella_t casella = piano[r*COLS + mossa_c];
        if (casella==VUOTO) {
            piano[r*COLS + mossa_c] = player;
            return r;
        }
    }
    /* nessuna casella trovata */
    return -1;
}

bool_t mossa_valida(piano_t piano, int ROWS, int COLS, int mossa_c) {
    casella_t casella = piano[0*COLS + mossa_c];
    return casella==VUOTO;
}

bool_t controlla_linea(piano_t piano, int ROWS, int COLS, int mossa_r, int mossa_c,
                       int dir_x, int dir_y) {
    int count = 0, delta;
    casella_t player = piano[(mossa_r)*COLS + mossa_c];

    /* Esplora le caselle 3 prima e 3 dopo lungo la direzione dir_x, dir_x
     * in cerca di 4 caselle consecutive uguali a player */
    for (delta=-3; delta <= 3 && count < 4; delta++) { /* esci se vengono trovati 4 consecutivi */
        if ((mossa_r + delta * dir_y) >= 0 && (mossa_r + delta * dir_y) < ROWS &&
             (mossa_c + delta * dir_x) >= 0 && (mossa_c + delta * dir_x) < COLS ) {
            casella_t casella = piano[(mossa_r + delta * dir_y) * COLS + (mossa_c + delta * dir_x)];
            if (casella == player)
                count++;   /* un altro consecutivo */
            else
                count = 0; /* casella vuota o altro giocatore */
        }
    }
    /* true se vengono trovati 4 elementi consecutivi, false altrimenti */
    if (count==4)
        return TRUE;
    else
        return FALSE;
}

bool_t vincente(piano_t piano, int ROWS, int COLS, int mossa_r, int mossa_c) {
    int dir_x, dir_y;
    for (dir_x=-1; dir_x <= 1; dir_x++) {
        for (dir_y=0; dir_y <= 1; dir_y++) { /* non c'è bisogno di dir_y=-1 per simmetria */
            if (dir_x != 0 || dir_y != 0) {   /* incrementa in almeno una direzione */
                if ( controlla_linea(piano, ROWS, COLS, mossa_r, mossa_c, dir_x, dir_y) )
                    return TRUE;
            }
        }
    } /* il caso dir_x=1,dir_y=0 è un doppione di dir_x=-1,dir_y=0 , a voi trovare alternative. */
    return FALSE;
}



int cpu_play_minmax(piano_t piano, int ROWS, int COLS, casella_t cpu_player,
             casella_t turno, int mossa_c, int depth) {
    int mossa_r;
    int best_score = 0;

    /* no more recursion */
    if (depth==0) return 0;

    /* fai la mossa */
    mossa_r = mossa(piano, ROWS, COLS, mossa_c, turno);
    if ( vincente(piano, ROWS, COLS, mossa_r, mossa_c) ) {
        if (cpu_player==turno)
            best_score = 1;
        else
            best_score = -1;
    } else {
        /* ricorsione */
        int nuova_mossa;
        int prox_turno = prossimo_turno(turno);
        int *scores = (int*) malloc(7*sizeof(int));
        int s, num_scores = 0;
        for (nuova_mossa=0; nuova_mossa<COLS; nuova_mossa++) {
            if ( mossa_valida(piano, ROWS, COLS, nuova_mossa) ) {
                scores[num_scores++] = cpu_play_minmax(piano, ROWS, COLS, cpu_player,
                                                prox_turno, nuova_mossa, depth - 1);
            }
        }
        best_score = scores[0];
        for (s=1; s<num_scores; s++) {
            /* printf(">>> %d %d %d\n", depth, s, scores[s]); */
            if (cpu_player==prox_turno) { /* maximize */
                if (scores[s]>best_score) best_score = scores[s];
            } else { /* minimize */
                if (scores[s]<best_score) best_score = scores[s];
            }
        }
        free(scores);
    }
    /* undo della mossa */
    piano[mossa_r*COLS + mossa_c] = VUOTO;

    return best_score;
}

/*
 * Score = 0 if max depth
 * Score = 1 if win
 * Score = -1 if loss
 * Score = sum( Score(other move) fore each other move )
 * investigate min_max strategy for further improvements...
 */

int cpu_play(piano_t piano, int ROWS, int COLS, casella_t cpu_player,
             casella_t turno, int mossa_c, int depth) {
    int mossa_r;
    int vittorie = 0;

    /* no more recursion */
    if (depth==0) return 0;

    /* fai la mossa */
    mossa_r = mossa(piano, ROWS, COLS, mossa_c, turno);
    if ( vincente(piano, ROWS, COLS, mossa_r, mossa_c) ) {
        if (cpu_player==turno)
            vittorie++;
        else
            vittorie--;
    } else {
        /* ricorsione */
        int nuova_mossa;
        for (nuova_mossa=0; nuova_mossa<COLS; nuova_mossa++) {
            if ( mossa_valida(piano, ROWS, COLS, nuova_mossa) ) {
                vittorie += cpu_play(piano, ROWS, COLS, cpu_player,
                                     prossimo_turno(turno), nuova_mossa, depth - 1);
            }
        }
    }
    /* undo della mossa */
    piano[mossa_r*COLS + mossa_c] = VUOTO;

    return vittorie;
}

/* TODO: you can improve the code by avoiding to have two functions with two loops,
 * consider for instance having a functions that returns a pair (best_score, best_move) */
int cpu_strategy(piano_t piano, int ROWS, int COLS, casella_t cpu_player) {
    int best_move  = -1;
    int best_score = 0;
    int mossa_c;

    for (mossa_c=0; mossa_c<COLS; mossa_c++) {
        if ( mossa_valida(piano, ROWS, COLS, mossa_c) ) {
            int score = cpu_play(piano, ROWS, COLS, cpu_player, cpu_player, mossa_c, 8);
            /* printf("  >> CPU move %d (score: %d) \n", mossa_c, score); */
            if (best_move == -1 || score > best_score) {
                best_move = mossa_c;
                best_score = score;
            }
        }
    }

    printf("CPU suggestion %d (score: %d) \n", best_move, best_score);
    return best_move;
}


int main() {
    const int ROWS = 6;
    const int COLS = 7;
    piano_t piano = (piano_t) malloc(ROWS*COLS*sizeof(casella_t));

    int mossa_c, mossa_r;
    bool_t end_of_game = FALSE;
    bool_t vittoria;
    casella_t turno = PLAYER_1;

    /* inizializzare */
    init(piano, ROWS, COLS);

    /* visualizzare */
    stampa(piano, ROWS, COLS);

    while (!end_of_game) {
        /* inserire una mossa */
        if (turno==PLAYER_1) printf("Turno X - ");
        else printf("Turno O - ");
        printf("Selezione una colonna: ");
        scanf("%d", &mossa_c);
        mossa_r = mossa(piano, ROWS, COLS,
                        mossa_c, turno);
        /* visualizzare */
        stampa(piano, ROWS, COLS);

        /* vincente */
        vittoria = vincente(piano, ROWS, COLS,
                            mossa_r, mossa_c);
        if (vittoria) {
            printf("VITTORIA!!!\n");
            end_of_game = TRUE;
        } else {
            /* cambia turno */
            turno = prossimo_turno(turno);
        }
        cpu_strategy(piano, ROWS, COLS, turno);
    }

    free(piano);

    return 0;
}
