

<p align=center> <h2 align=center>custom-thumbnail</h2></p>

<p align=center>Recursively creates custom thumbnails keeping aspect ratio and directory structure unchanged :)</p>
<p align=center> <b> inplace conversion . configurable </b>  </p>
<p align=center> keep original directory structure while wiriting under a seperate directory</p>

<p align=center>
  <img align=center src=http://hits.dwyl.com/deep5050/custom-thumbnail.svg" />
  <img align=center src="https://img.shields.io/github/v/release/deep5050/custom-thumbnail?style=flat-square" />                                                                  

</p>


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
          inplace: "disable" # 'enable' / "disable" [ write thumbnails at their origin path (replace) ], if disabled writes under '.thumbnails' directory 
          baseheight_width: "500" # (px) max limit of height/width
      - name: Commit & Push changes
        uses: mikeal/publish-to-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```
