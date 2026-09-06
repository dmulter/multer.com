# multer.com

The Multer website is built on [Hugo](https://gohugo.io/) with the [PaperMod](https://github.com/adityatelange/hugo-PaperMod/) theme. I
have a few customizations on the theme via shortcodes and partials. I'm busy
porting the old content from multer.com to this new site, so you can expect
some significant changes as I continue to make progress.

## Notes

A few things when working with the site:

- GitHub actions will auto build and deploy the site to GitHub Pages.
  Eventually I'll configure the site to override the existing multer.com
  site.
- You can run the site locally using the `run.sh` script.
- I use the ImageMagik to convert all JPG images before commiting to the repo.
`magick mogrify -path XXX -resize 1200x -strip -quality 80 XXX`
- Some stories use WEBP images.
- All images are stored in a public AWS S3 bucket.
- The current website genealogy data is moving to WikiTree, so nothing will be
  in this repo.
- I use the `ignoreFiles` configuration to avoid processing of stories I'm in
  the middle if importing from the old site.
- Use `update.sh` to update submodules, which currently consist of the PaperMod
  theme only.
- Note that `build.sh` and `deploy.sh` are unused. They were used for direct to
  AWS S3 deploys that I might use in the future.
