#include <stdio.h>
#include <stdbool.h>

#define max_lista 100

typedef struct lista
{
    int vetor[max_lista];
    int tamanho;
} lista;

void criar_lista(lista *l)
{
    l->tamanho = 0;
}

void inserir_lista(lista *l, int valor)
{
    l->vetor[l->tamanho] = valor;
    l->tamanho++;
}

void imprimir_lista(lista *l)
{
    for (int i = 0; i < l->tamanho; i++)
    {
        printf("%d ", l->vetor[i]);
    }
    printf("\n");
}

bool verificar_ordenada(lista *l)
{
    if (l->tamanho <= 1)
    {
        return true;
    }

    bool crescente = true;
    for (int i = 0; i < l->tamanho - 1; i++)
    {
        if (l->vetor[i] > l->vetor[i + 1])
        {
            crescente = false;
            break;
        }
    }

    if (crescente)
    {
        return true;
    }

    bool decrescente = true;
    for (int i = 0; i < l->tamanho - 1; i++)
    {
        if (l->vetor[i] < l->vetor[i + 1])
        {
            decrescente = false;
            break;
        }
    }

    return decrescente;
}

lista copiar_lista(lista *l1)
{
    lista l2;
    criar_lista(&l2);
    for (int i = 0; i < l1->tamanho; i++)
    {
        inserir_lista(&l2, l1->vetor[i]);
    }
    return l2;
}

lista copiar_lista_remover_duplicados(lista *l1)
{
    lista l2;
    criar_lista(&l2);

    for (int i = 0; i < l1->tamanho; i++)
    {
        int aux = l1->vetor[i];
        bool ja_existe = false;
        for (int j = 0; j < l2.tamanho; j++)
        {
            if (l2.vetor[j] == aux)
            {
                ja_existe = true;
                break;
            }
        }

        if (!ja_existe)
        {
            inserir_lista(&l2, aux);
        }
    }
    return l2;
}

lista inverter(lista *l1){
    lista l2;
    criar_lista(&l2);

    for (int i = l1->tamanho - 1; i>= 0; i--){
        inserir_lista(&l2, l1->vetor[i]);
    }
    return l2;
}

void inverter_origem(lista *l1){
    for (int i = 0; i < l1->tamanho / 2; i++){
        int aux = l1->vetor[i];
        l1->vetor[i] = l1->vetor[l1->tamanho - 1 - i];
        l1->vetor[l1->tamanho - 1 - i] = aux;
    }
}

int main()
{
    lista l;
    criar_lista(&l);
    inserir_lista(&l, 10);
    inserir_lista(&l, 20);
    inserir_lista(&l, 30);
    inserir_lista(&l, 40);
    inserir_lista(&l, 50);
    inserir_lista(&l, 60);
    imprimir_lista(&l);

    // lista l2 = copiar_lista_remover_duplicados(&l);
    // lista l2 = inverter(&l);
    inverter_origem(&l);
    imprimir_lista(&l);
    return 0;
}