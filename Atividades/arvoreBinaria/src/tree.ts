import { Knot } from './knot'

export class Tree {
  raiz: Knot | undefined

  inserir(valor: number): void {
    if (this.raiz === undefined) this.raiz = new Knot(valor)
    else {
      this.inserir_recursivo(this.raiz, valor)
    }
  }

  inserir_recursivo(noAtual: Knot, valor: number): void {
    console.log('Inserindo', valor, 'em', noAtual.valor)
    if (valor === noAtual.valor) {
      return
    }

    if (valor < noAtual.valor) {
      if (noAtual.esquerda === undefined) {
        noAtual.esquerda = new Knot(valor)
      } else {
        this.inserir_recursivo(noAtual.esquerda, valor)
      }
    } else {
      if (noAtual.direita === undefined) {
        noAtual.direita = new Knot(valor)
      } else {
        this.inserir_recursivo(noAtual.direita, valor)
      }
    }
  }

  // emOrdem(): void{
  //     this.emOrdemRecursivo(this.raiz)
  //     console.log()
  // }
  // emOrdemRecursivo(no: Knot | undefined): void{
  //     if (no) {
  //         this.emOrdemRecursivo(no.esquerda)
  //         console.log(no.valor)
  //         this.emOrdemRecursivo(no.direita)
  //     }
  // }
  imprimir(
    no: Knot | undefined = this.raiz,
    prefixo: string = '',
    isEsquerda: boolean = true
  ): void {
    if (no === undefined) return

    console.log(
      prefixo + (prefixo ? (isEsquerda ? '├── ' : '└── ') : '') + no.valor
    )

    const novoPrefixo =
      prefixo + (prefixo ? (isEsquerda ? '│   ' : '    ') : '')

    if (no.esquerda || no.direita) {
      this.imprimir(no.esquerda, novoPrefixo, true)
      this.imprimir(no.direita, novoPrefixo, false)
    }
  }
}
