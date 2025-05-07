export class Knot {
  valor: number
  esquerda: Knot | undefined
  direita: Knot | undefined

  constructor(valor: number) {
    this.valor = valor
    this.esquerda = undefined
    this.direita = undefined
  }
}
