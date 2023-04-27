# Laboratorio 3 - JavaScript

## Clase 01 - Ciclos

### Ciclo While

```javascript
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;
}
console.log("Fin del ciclo while");
```

### Ciclo Do While

```javascript
let conteo = 0;
do {
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log("Fin del ciclo do while");
```

### Ciclo For

```javascript
for(let contando = 0; contando < 3; contando++){
    console.log(contando);
}
console.log("Fin del ciclo for");
```

### Palabra reservada break

```javascript
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando);
        break;
    }i
}
console.log("Termina el ciclo al encontrar el primer numero Par");
```

### Palabra reservada continue

```javascript
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue; // ir a la siguiente iteration (ignora los numeros impares)
    }
    console.log(contando);
}
console.log("Termina el ciclo ");
```

### Etiquetas Lebels (es recomendada no utilizarla)

```javascript
inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue inicio; // ir a la siguiente iteration (ignora los numeros impares)
    }
    console.log(contando);
}
console.log("Termina el ciclo ");
```

### Tarea

Todos los ejercicio hechos en otros lenguajes traerlos aquí con la sintaxis de JavaScript, por supuesto ejercicios de ciclos.

## Clase 02 - Arreglos

### Creación de un array

#### Sintaxis vieja

```javascript
let autos = new Array('Ferrari','Renault','Bmw');
```

#### Sintaxis actual

```javascript
const autos = ['Ferrari','Renault','Bmw'];
```

### Recorremos los elementos del array

```javascript
console.log(autos[0]);
console.log(autos[1]);
console.log(autos[2]);

for (let i = 0; i < autos.length; i++){
    console.log(i+' : '+autos[i]);
}
```

### Modificar un elemento del array

```javascript
autos[1] = 'volvo';
console.log(autos[1]);  // volvo
```

### Agregar un elemento al array

```javascript
autos.push('Audi');
console.log(autos.length);   // 4
```

#### Otra forma de agregar un elemento a un array

```javascript
autos.push('Audi');
console.log(autos.length);  // (5) ['Ferrari', 'volvo', 'Bmw', 'Audi', 'Porche']
```

#### Tercera forma de agregar un elemento a un array

Hay que tener cuidado con esta forma por que agrega espacios en blanco y genera mucho espacio de memoria

```javascript
autos[3] = 'chevrolet';
console.log(autos);
```

### Como preguntar si es una array

```javascript
console.log(Array.isArray(autos)); // true
```

#### Otra forma

```javascript
console.log(autos instanceof Array); // true
```
