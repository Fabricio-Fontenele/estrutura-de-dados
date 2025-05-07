export class TreeNode {
  valor: number;
  esquerda: TreeNode | null;
  direita: TreeNode | null;

  constructor(valor: number, esquerda: TreeNode | null = null, direita: TreeNode | null = null) {
    this.valor = valor;
    this.esquerda = esquerda;
    this.direita = direita;
  }
}
