    function colorPalette(id) {
        var palettes = [["#3dc8ff", "#ff3d87", "#ff703d", "#ffc83d", "#e1ff3d"],
            ["#493548", "#4b4e6d", "#6a8d92", "#80b192", "#a1e887"],
            ["#335c67", "#fff3b0", "#e09f3e", "#9e2a2b", "#540b0e"],
            ["#4d9de0", "#e15554", "#e1bc29", "#3bb273", "#7768ae"],
            ["#202030", "#39304a", "#635c51", "#7d7461", "#b0a990"],
            ["#f1e0c5", "#c9b79c", "#71816d", "#342a21", "#da667b"],
            ["#7b7554", "#17183b", "#a11692", "#ff4f79", "#ffb49a"]];
        return palettes[(id % palettes.length)];
    }
