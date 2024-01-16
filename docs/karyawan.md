## karyawan API Spec

## findAll karyawan

-- Endpoint : GET /api/karyawans

Respone Body (Success)

```json
{
  "data": [
    {
      "name": "bambang",
      "jabatan": "bandung",
      "karyawan": 1
    }
  ]
}
```

Respone Body (Faild)

```json
{
  "message": "karyawan Not Found"
}
```

## find One karyawan

-- Endpoint : GET /api/karyawans/:pk

Respone Body (Success)

```json
{
  "name": "bambang",
  "jabatan": "bandung",
  "kantor": 1
}
```

Respone Body (Faild)

```json
{
  "message": "karyawan Not Found"
}
```

## create-karyawan

-- Endpoint : POST /api/karyawans

Request Body :

```json
{
  "name": "bambang",
  "jabatan": "bandung",
  "kantor": 1
}
```

Respone Body (Success)

```json
{
  "name": "bambang",
  "jabatan": "bandung",
  "kantor": 1
}
```

Respone Body (Faild)

```json
{
  "message": "karyawan Not Found"
}
```

## Edit karyawan

-- Endpoint : PUT /api/karyawans/:pk

Request Body :

```json
{
  "name": "bambang update",
  "jabatan": "bandung",
  "kantor": 1
}
```

Respone Body (Success)

```json
{
  "name": "bambang update",
  "jabatan": "bandung",
  "kantor": 1
}
```

Respone Body (Faild)

```json
{
  "message": "karyawan Not Found"
}
```

## Delete-karyawan

-- Endpoint : Delete /api/karyawans/:pk

Response Body (Success)

```json
{
  "message": "OK"
}
```
