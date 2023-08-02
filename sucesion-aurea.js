/*Resolución del ejercicio 3 : el patrón que siguen los números del array tiende a ser el producto del número áureo por el número anterior*/

let array_inicial=[1, 1.618, 2.618, 4.236];
console.log('Numeros iniciales:' + array_inicial);

/* en la letra del ejercicio se nombra " paso dorado" haciendo referencia al número aúreo= phi"*/

const phi= (1+ Math.sqrt(5))/2;  /*phi está definido matemáticamente a través esta expresión*/


let cantNumeros_siguientes= 10; /* Cntidad de números que quiero ver despues de los iniciales */

for (let i=0; i < cantNumeros_siguientes; i++){
    let elemento_siguiente= array_inicial[array_inicial.length -1] * phi; /*multiplica el valor anterior x el aúreo para obtener el siguiente en el array*/ 
    array_inicial.push(elemento_siguiente); /* push() es un método de los array que agrega un elemento al final del array*/
    console.log(elemento_siguiente.toFixed(4)); /* toFixed() es un método para aproximar un número con cierta cantidad de decimales*/
}

