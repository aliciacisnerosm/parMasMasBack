# PAR++

El lenguaje PAR++ permite declarar variables de tipo int, float y char, realizar operaciones aritméticas, lógicas y relacionales. Permite la declaración de funciones de estos 3 tipos además de la función void. Entre sus estatutos permite la asignación de valores a una variable, lectura de una variable, escritura de variables, constantes y strings, decisiones de tipo if e if else, ciclos while y for, así como la declaración y manipulación de variables estructuradas de una sola dimensión.

## Equipo Par++
Nombre | Matrícula
------------ | -------------
Alicia Guadalupe Cisneros Morales | A01281991
Martha Cristina Arnaud Pacheco | A01410560

## Requerimientos para la utilización del lenguaje 
* Python 3
* React-Native
* Flask

## Instrucciones para correr el compilador
1. . venv/bin/activate
2. flask run

## Instrucciones para utilizar la aplicación móvil
1. npm install
2. npx react-native run-ios

### Estructura general del lenguaje Par++

```
program nombrePrograma :
  <Declaración de variable globales>
  <Declaración de funciones>
  main(){
    <Estatutos>
  }
```
 ### Declaración de variables
 ```
 var tipo1: var1, var2[n] & var tipo2: var3 & tipo3: var4;
 ```

 Tipos de variables:
 * int
 * float
 * char

 ### Declaración de funciones

 ```
 tipo id (tipo parametro1, tipo parametro2){
   <Declaración de variables>
   <Estatutos>
 }
 ```
 Tipos de funciones:
 * int
 * float
 * char
 * void

### Estatutos
* Asignación
* Llamadas a funciones
* Lectura (read)
* Escritura (write)
* Decision (if & if else)
* Repetición (for & while)

### Asignación

```
operadorizq = operadorderecho;
```

### Llamada a funciones
```
  nombreFuncion(parámetro 1);
```
* La función a llamar tiene que estar declarada en el código.
* Las llamadas pueden hacerse dentro de si misma, otra función o desde el main.

### Lectura
````
read(variable);
````
* La variable tiene que estar previamente declarada por el usuario.
* Toma el valor que el usuario manda como entrada en el programa.

### Escritura
````
write(x);
````
* Se pueden imprimir variables, arreglos, constantes, strings (letreros) y resultados de expresiones.
* Será desplegado en la interfaz móvil.

### Decisión
```
if(expresión){
    estatutos;
};


if(expresión){
    estatutos;
}
else{
    estatutos;
};
```
* La expresión que reciben estos estatutos de decisión don del tipo booleana.

### Repetición
```
for(x =lnf to lsup){
  estatutos;
}
```
* Repite desde el límite inferior hasta el límite superior brincando de uno en uno.

```
while(expresión){
  estatutos;
}
```
* Repite los estatutos mientras la expresión sea verdadera


### Operadores

##### Aritméticos
* Suma (+)
* Resta (-)
* Multiplicación (*)
* División (/)

##### Lógicos
* and
* or

##### Relacionales
* '>'
* '<'
* '=='
* '<>'
* '<='
* '>='


* Se manejan las prioridades tradicionales, pueden ser alteradas mediante el uso de paréntesis ( )