

<p align=center> <h2 align=center>custom-thumbnail</h2></p>

<p align=center>Recursively creates custom thumbnails keeping aspect ratio intact :)</p>

```yaml
name: custom-thumbnail
on: [push]

jobs:
  build:
    name: custom-thumbnail
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: custom-thumbnail
        uses: deep5050/custom-thumbnail@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN}}
          inplace: True
      - name: Commit & Push changes
        uses: mikeal/publish-to-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```
