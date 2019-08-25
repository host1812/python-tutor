playlist = {
    "title" : "Sleep",
    "songs" : [
        {
            "title" : "Tale Super",
            "duration" : "1:06",
            "genre" : "Trance"
        },
        {
            "title" : "Kak Ya Poshel V Les",
            "duration" : "35:54",
            "genre" : "Audioskazka"
        }
    ]
}

title = playlist.get("songs")[1].get("title")
print(title)