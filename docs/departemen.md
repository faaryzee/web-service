## departemens API Spec

## findAll departemens

-- Endpoint : GET /api/departemens

Respone Body (Success)

```json
{
  "data": [
    {
      "id": 1,
      "name": "bandung"
    }
  ]
}
```

Respone Body (Faild)

```json
{
  "message": "departemens Not Found"
}
```

## find One departemens

-- Endpoint : GET /api/departemens/:pk

Respone Body (Success)

```json
{
  "id": 1,
  "name": "bandung"
}
```

Respone Body (Faild)

```json
{
  "message": "departemens Not Found"
}
```

## create-departemens

-- Endpoint : POST /api/departemens

Request Body :

```json
{
  "name": "bandung"
}
```

Respone Body (Success)

```json
{
  "id": 1,
  "name": "bandung"
}
```

Respone Body (Faild)

```json
{
  "message": "departemens Not Found"
}
```

## Edit departemens

-- Endpoint : PUT /api/departemens/:pk

Request Body :

```json
{
  "name": "bandung"
}
```

Respone Body (Success)

```json
{
  "id": 1,
  "name": "bandung"
}
```

Respone Body (Faild)

```json
{
  "message": "departemens Not Found"
}
```

## Delete-departemens

-- Endpoint : Delete /api/departemens/:pk

Response Body (Success)

```json
{
  "message": "OK"
}
```
