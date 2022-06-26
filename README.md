
# ToDo Api Challenge

Para este Challenge se pidio realizar un desarrollo en Python y Django en el cual
mediante Apis se puede gestionar un ToDo List.


## API Reference



#### lisado completo de tareas

```http
  GET api/task/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
|           |          |                            |

#### Post tareas

```http
  POST api/task/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
|     task  |string    | Titulo de la tarea         |
|description|string    | Descripcion de la tarea    |
|completed  |bool      | Saber si se completo o no  |

#### Get tareas

```http
  GET api/task/<int:pk>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| pk        |int    | **Required**. pk de la tara a consultar |


#### Update tareas

```http
  POST api/task/<int:pk>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| pk        |int    | **Required**. pk de la tara a updatear |
|     task  |string    | Titulo de la tarea         |
|description|string    | Descripcion de la tarea    |
|completed  |bool      | Saber si se completo o no  |

#### Delete tareas

```http
  DELETE api/task/<int:pk>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| pk        |int    | **Required**. pk de la tara a eliminar |


```http
  GET 'api/task_detail/<str:nameTask>'
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| nameTask  |string    | **Required**. string contenido en el titulo buscado |





## Installation

Para utilizar el proyecto se debe clonar e instalar las dependencias necesarias se debe utilizar

```bash
  git clone 
  pip install -r requirements.txt
```
    
## Ejecutar proyecto localmente

Clonar proyecto

```bash
  git clone https://link-to-project
```

Directorio

```bash
  cd \Invera\Challenge\Invera
```

Instalar dependencias

```bash
  pip install -r requirements.txtl
```

Iniciar pagina

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```

