================

#UDP Modelos Estocasticos 2013 

#### VmusicWebService  V 0.0.1

<p>Guillermo Labra - Daniel Roble </p>
memolabra@me.com - daniel12dar@gmail.com

#####Descripción:
La aplicación consiste compartir nombres de canciones a traves de twitter  con un hastag de tal forma de poder con ellas generar un proceso de infeccion descrito en el paper "On Measurement of Influence in Social Networks" mediante el cual se encuentre el nodo(usuario) que posee la mayor probablidad de propagacion dentro de la red en base a los que se a propagado.
##### Descripciíon breve del actividades:
La aplicacion consiste de dos elementos fundamentales, webservice escrito es ```Python 2,7``` en el cual se encuentra la logica de extraccion de datos desde twitter utilizando la api ```Twython```, la logica de el proceso de infeccion y la busqueda de las canciones compartidas con la api de ```Rdio``` , todo este proceso terminado es enviando como bjetos  ```Json``` a el segundo elemento principal, una aplacion movil nativa escrita en ```Objetive-c ```para iPhone.
#### Iniciar aplicacion:
Para iniciar la aplicacion basta con copiar los archivos de este git a una carpeta y correr bajo ```Python 2,7``` el archivo ```run.py``` el cual, como fue descrito anteriormente buscara en twitter los tweet con el hashtag de la aplicacion ( #iOSVmusic ) cabe recalcar que los tweet antiguos son reciclados por twitter, por lo que si ha pasado un tiempo considerable no apareceran los tweet con el hashtag con los que habria que twetear de nuevo mensajes con el formato de nuestra aplicacion [ mensaje personal [:] [nombre cancion] [-] [artista] [#iOSVmusic] ]. 
