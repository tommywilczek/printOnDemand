
for filename in /Users/tommywilczek/Documents/Projects/patternPop/generatedPatterns/*.png; do 
    echo $filename
    # mirrorName="$filename-mirror"
    wordToInsert="_mirror"
    match=".png"
    mirrorName=${filename%%"${match}"*}${wordToInsert}${filename#*"${filename%%"${match}"*}"}
    # ^ Inserts the mirror tag in front of the .png in the filename
    echo $mirrorName
     cp $filename $mirrorName
     sips -f horizontal $mirrorName
done 