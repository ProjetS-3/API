# API
## How to use

### POST

Post requests are made on endpoint '/reservation'

#### Headers
**In headers, dont forget to put the content-type (application/json) and your api key (push new one if you don't have one) under "x-api-key"**

#### Body
The body of your request will be in format:
```json
{
  "product_id": "05",
  "quantity": 1
}
```

#### Return
```json
{
    "reservation_id": "id of your reservation"
}
```


### GET

Get requests are made on endpoint '/distribution/{reservation_id}'

#### Headers
**In headers, dont forget to put your api key under "x-api-key"**

#### Return
**Reservation exists**
```json
{
  "exists": true,
  "product_id": 05,
  "quantity": 1
}
```

**Reservation doesn't exists**
```json
{
  "exists": false
}
```


