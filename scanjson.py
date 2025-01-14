from openapi_parser import parse

specification = parse('openapi.json')

urls = [x.url for x in specification.paths]
proxy = 'http://127.0.0.1:8080'

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTYyNDI2MjIsImlhdCI6MTUxNjIzOTAyMiwibmFtZSI6IkpvaG4gRG9lIiwic3ViIjoiMmNiMzA3YmEtYmI0Ni00MTk0LTg1NGYtNDc3NDA0NmQ5YzliIn0.SCC35SSgMSMr0kV1i_TuPAhiSGtsC1cFGCfvaus5GyU'

print(urls)

For url in urls
`vulnapi scan curl 'http://localhost:5001{$url}' -H 'accept: application/json Authorization: Bearer {token} ' --proxy $proxy `
