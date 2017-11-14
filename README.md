# GitHubRankingsSpain-badge

🛡️ Insignias del ranking de desarrolladores españoles en GitHub

Actualmente en desarrollo... 🛠️


### Instalación

Puedes instalarlo desde el código fuente con:

``` 
$ git clone https://github.com/RDCH106/GitHubRankingsSpain-badge.git --recursive
$ cd GitHubRankingsSpain-badge/service
$ pip install -r requirements.txt
```


### API

#### Servicio de insignias

Formato de petición: `<host>:<port>/badge/<region_name>/<github_user>`

- `<host>`: IP o dominio de la máquina que aloja el servicio
- `<port>`: Puerto en el que se sirve el servicio
- `<region_name>`: Ver tabla de regiones para conseguir la insignia de la región deseada
- `<github_user>`: Usuario GitHub del que se quiere obtener la insignia

**Tabla de Regiones** :es:

| Región             | region_name        |
|--------------------|--------------------|
| España             | spain              |
| Andalucía          | andalucia          |
| Almería            | almeria            |
| Cádiz              | cadiz              |
| Córdoba            | cordoba            |
| Granda             | granada            |
| Huelva             | huelva             |
| Jaén               | jaen               |
| Málaga             | malaga             |
| Sevilla            | sevilla            |
| Aragón             | aragon             |
| Huesca             | huesca             |
| Teruel             | teruel             |
| Zaragoza           | zaragoza           |
| Asturias           | asturias           |
| Cantabria          | catanbria          |
| Castilla y León    | castillayleon      |
| Ávila              | avila              |
| Burgos             | burgos             |
| León               | leon               |
| Palencia           | palencia           |
| Salamanca          | salamanca          |
| Segovia            | segovia            |
| Soria              | soria              |
| Valladolid         | valladolid         |
| Zamora             | zamora             |
| Castilla-La Mancha | mancha             |
| Albacete           | albacete           |
| Ciudad Real        | ciudadreal         |
| Cuenca             | cuenca             |
| Guadalajara        | guadalajara        |
| Toledo             | toledo             |
| Cataluña           | catalonia          |
| Barcelona          | barcelona          |
| Gerona             | girona             |
| Lérida             | lleida             |
| Tarragona          | tarragona          |
