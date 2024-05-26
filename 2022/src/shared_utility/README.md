# Shared Utilities

## Learnings & References

When running:

```python
for line in urllib.request.urlopen(url):
    print(line.decode('utf-8')) #utf-8 or iso8859-1 or whatever the page encoding scheme is
```

I got error:

```text
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)>
```

So I googled that error, found this StackOverflow answer by e-satis ([formationspython.com](https://formationspython.com/)): https://stackoverflow.com/a/1393367/4718936

```python
import urllib.request  # the lib that handles the url stuff

for line in urllib.request.urlopen(target_url):
    print(line.decode('utf-8')) #utf-8 or iso8859-1 or whatever the page encoding scheme is
```
