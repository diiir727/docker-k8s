##### Описание

Идемпотентность реализована с помощью ключа идемпотентности.

`helm install mycache app-chart/`
##### Результаты тестирования

```
idempotent-orders

→ get all orders
  GET http://arch.homework/otusapp/orders?user=1 [200 OK, 699B, 88ms]
  ✓  size

→ create first order
  POST http://arch.homework/otusapp/orders/pay [200 OK, 338B, 30ms]

→ try duplicate
  POST http://arch.homework/otusapp/orders/pay [200 OK, 338B, 39ms]

→ new order not created
  GET http://arch.homework/otusapp/orders?user=1 [200 OK, 766B, 38ms]
  ✓  create just one order

┌─────────────────────────┬───────────────────┬──────────────────┐
│                         │          executed │           failed │
├─────────────────────────┼───────────────────┼──────────────────┤
│              iterations │                 1 │                0 │
├─────────────────────────┼───────────────────┼──────────────────┤
│                requests │                 4 │                0 │
├─────────────────────────┼───────────────────┼──────────────────┤
│            test-scripts │                 6 │                0 │
├─────────────────────────┼───────────────────┼──────────────────┤
│      prerequest-scripts │                 5 │                0 │
├─────────────────────────┼───────────────────┼──────────────────┤
│              assertions │                 2 │                0 │
├─────────────────────────┴───────────────────┴──────────────────┤
│ total run duration: 375ms                                      │
├────────────────────────────────────────────────────────────────┤
│ total data received: 1.2KB (approx)                            │
├────────────────────────────────────────────────────────────────┤
│ average response time: 48ms [min: 30ms, max: 88ms, s.d.: 22ms] │
└────────────────────────────────────────────────────────────────┘

```


