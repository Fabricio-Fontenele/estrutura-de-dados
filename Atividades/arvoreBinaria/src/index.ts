import { Tree } from "./tree";

const arvore = new Tree()

const elementos = [1, 2, 3, 14, 15, 28, 32, 45, 56, 992]

for (const v of elementos ) {
    arvore.inserir(v)
}
arvore.imprimir()