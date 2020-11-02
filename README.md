
![custom-thumbnail](https://socialify.git.ci/deep5050/custom-thumbnail/image?description=1&font=Bitter&language=1&owner=1&pattern=Charlie%20Brown&theme=Light)


<p align=center> <b> inplace conversion . configurable </b>  </p>


<p align=center>
 <!-- <img align=center src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdeep5050%2Fcustom-thumbnail"/>                         -->
  <img align=center  src="https://visitor-badge.laobi.icu/badge?page_id=deep5050.custom-thumbnail" alt="Visitors">
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
## Bugs
[submit bugs here](https://github.com/deep5050/custom-thumbnail/issues)



## Want To Contribute?

All kinds of contributions are welcome :raised_hands:! The most basic way to show your support is to star :star2: the project, or to raise issues :speech_balloon: You can also support this project by [**becoming a sponsor on GitHub**](https://github.com/sponsors/deep5050) :clap: or by making a [Paypal donation](https://www.paypal.me/deep5050) to ensure this journey continues indefinitely! :rocket:

Thanks again for your support, it is much appreciated! :pray:

## Related Works

[qikQR](https://github.com/deep5050/qikQR) . [autobadge](https://github.com/deep5050/autobadge) . [qikstart](https://github.com/deep5050/qikstart)
