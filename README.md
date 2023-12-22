```shell
# Generate a RSA private key, of size 2048 

openssl genrsa -out jwt-private.pem 2048

```

```shell
    # Generate a RSA public key
openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem 
```
