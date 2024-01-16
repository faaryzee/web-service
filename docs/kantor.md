## kantor API Spec

## findAll kantor

-- Endpoint : GET /api/kantors

Respone Body (Success)

```json
{
  "data": [
    {
      "title": "product",
      "lokasi": "bandung",
      "departemen": 1
    }
  ]
}
```

Respone Body (Faild)

```json
{
  "message": "kantor Not Found"
}
```

## find One kantor

-- Endpoint : GET /api/kantors/:pk

Respone Body (Success)

```json
{
  "title": "product",
  "lokasi": "bandung",
  "departemen": 1
}
```

Respone Body (Faild)

```json
{
  "message": "kantor Not Found"
}
```

## create-kantor

-- Endpoint : POST /api/kantors

Request Body :

```json
{
  "title": "product",
  "lokasi": "bandung",
  "departemen": 1
}
```

Respone Body (Success)

```json
{
  "title": "product",
  "lokasi": "bandung",
  "departemen": 1
}
```

Respone Body (Faild)

```json
{
  "message": "kantor Not Found"
}
```

## Edit kantor

-- Endpoint : PUT /api/kantors/:pk

Request Body :

```json
{
  "title": "product",
  "lokasi": "bandung",
  "departemen": 1
}
```

Respone Body (Success)

```json
{
  "title": "product",
  "lokasi": "bandung",
  "departemen": 1
}
```

Respone Body (Faild)

```json
{
  "message": "kantor Not Found"
}
```

## Delete-kantor

-- Endpoint : Delete /api/kantors/:pk

Response Body (Success)

```json
{
  "message": "OK"
}
```
