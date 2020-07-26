

<p align=center> <h2 align=center>custom-thumbnail</h2></p>

<p align=center>A GitHub action that recursively creates custom thumbnails keeping aspect ratio and directory structure unchanged :)</p>
<p align=center> <b> inplace conversion . configurable </b>  </p>
<p align=center> keep original directory structure while wiriting under output directory</p>

<p align=center>
  <!-- <img align=center src=http://hits.dwyl.com/deep5050/custom-thumbnail.svg" /> -->
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
          base_height_width: "500" # (px) max limit of height/width
          keep_dir_structure: "enable" # 'enable'/'disable' keep the input images directory structure while writing to .thumbnails directory
      - name: Commit & Push changes
        uses: mikeal/publish-to-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```

## License
>GNU Public License

>Copyright (c) 2020 Dipankar Pal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


