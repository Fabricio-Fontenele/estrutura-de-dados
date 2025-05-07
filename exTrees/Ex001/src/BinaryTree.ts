import { TreeNode } from "./treeNode";

export class BinaryTree {
  raiz: TreeNode | null;
  constructor(raiz: TreeNode | null = null) {
    this.raiz = raiz;
  }
  Insert(valor: number): void {
    if (this.raiz === null) {
      this.raiz = new TreeNode(valor);
    } else {
      this.inserirRecursivo(this.raiz, valor);
    }
  }
  inserirRecursivo(noAtual: TreeNode, valor: number): void {
    if (valor < noAtual.valor) {
      if (noAtual.esquerda === null) {
        noAtual.esquerda = new TreeNode(valor);
      } else {
        this.inserirRecursivo(noAtual.esquerda, valor);
      }
    } else {
      if (noAtual.direita === null) {
        noAtual.direita = new TreeNode(valor);
      } else {
        this.inserirRecursivo(noAtual.direita, valor);
      }
    }
  }
  contarElementos(noAtual: TreeNode | null = this.raiz): number {
    if (noAtual === null) {
      return 0;
    }

    return (
      1 +
      this.contarElementos(noAtual?.esquerda) +
      this.contarElementos(noAtual?.direita)
    );
  }
  maiorElemento(noAtual: TreeNode | null = this.raiz): number {
    if (noAtual === null) throw new Error("node is null");
    while (noAtual.direita != null) {
      noAtual = noAtual.direita;
    }
    return noAtual.valor;
  }

  menorElemento(noAtual: TreeNode | null = this.raiz): number {
    if (noAtual === null) throw new Error("node is null");
    while (noAtual.esquerda != null) {
      noAtual = noAtual.esquerda;
    }
    return noAtual.valor;
  }

  sumElements(noAtual: TreeNode | null = this.raiz): number {
    if (noAtual === null) {
      return 0;
    }

    return(
      noAtual.valor + this.sumElements(noAtual.esquerda) + this.sumElements(noAtual.direita)
    )
  }
}
