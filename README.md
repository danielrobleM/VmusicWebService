================

#UDP Modelos Estocasticos 2013 

#### VmusicWebService  V 0.0.1

<p>Guillermo Labra - Daniel Roble </p>
memolabra@me.com - daniel12dar@gmail.com

#####Descripción
La aplicación consiste compartir nombres de canciones a traves de twitter  con un hastag de tal forma de poder con ellas generar un proceso de infeccion descrito en el paper "On Measurement of Influence in Social Networks" mediante el cual se encuentre el nodo(usuario) que poose la mayor probablidad de propaacion dentro de la red en base a los que se a propagado.
##### Descripciíon breve del  actividades. 
La aplicacion consiste de dos  elementos fundamentales, webservice escrito es ```Python 2,7``` en el cual se encuentra la logica de extraccion de datos desde twitter utilizando la api ```Nombre de la api```, la logica de el proceso de infeccion y la busqueda de las canciones compartidas en la api de ```rdio``` , todo este procso terminando enviando data objetos  ```Json``` a el segundo elemento principal, una aplacion movil nativa escrita ```objetive-c ```para iPhone.
