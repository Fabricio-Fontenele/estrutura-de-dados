import { BinaryTree } from "./BinaryTree";

const arvore = new BinaryTree()
arvore.Insert(4)
arvore.Insert(48)
arvore.Insert(35)
arvore.Insert(1)
arvore.Insert(12)

console.log(arvore.contarElementos())
console.log(arvore.maiorElemento())
console.log(arvore.menorElemento())
console.log(arvore.sumElements())