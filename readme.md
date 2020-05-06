# Print On Demand

I wanted to see how tight I could make the feedback loop between product experimentation and discovering what my customers want. I created a program that creates its own designs, that were then put on to T-shirts, iPhone cases, fanny packs, and much more. These products were then put on Amazon to see which designs people liked more. The products were printed on demand, so I held no risk of lost inventory

Every step of the process was automated using Python and selenium

## Source Patterns

### Trianglify

run `index.html` on a live server to automatically generate and download patterns

Add a human element. Go through downloaded patterns and add cool sounding names.

run `sh flipImages.sh` to create copies and flip the original images

Upload to printful in bulk by selecting all images when uploading

## Use Printful to create products

run `python3 printfulAutomation.py` to run the browser automation tool that creates each printful item
