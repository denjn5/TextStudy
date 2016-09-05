## Memorizinator Game
A little memory game to help learn big ideas. Play it at https://bl.ocks.org/denjn5/878d1ef107a3962db18a01720a1b551f.

1. Game timer starts automatically (1.5 seconds / word).
2. Click the words in the proper order.
3. Game provides feedback about Win, Loss, Player Error.
4. Need a hint? (All are toggles)
   * _Show It_. Show the full quote.
   * _Say It_. Audio of the quote. [Works in Chrome/Safari.]
   * _Bold It_. The next correct word will be bolded.
   * _Punctiate It_. Turns on capitalization and punctuation.
5. Mistake? Incorrect answers are red. Click a circle to undo.
6. Select a new quote (top-right) or _Restart_ game (bottom-right).


## D3 Force Simulation Notes
* Memorizinator leverages the excellent D3 Force Simulation (version 4) mechanics.  It incorporates:
  * Multi-foci (with responsive width!)
  * Adds nodes
  * Adds links and removes links on the fly
  * Event handling
  * Text centered in nodes (overcomes Firefox vertical-align problem)

## Attributions
* D3: https://d3js.org/
* Framework: http://getskeleton.com/
* Icons: http://www.entypo.com/
* Colors: https://coolors.co/
  
## TODO
* Multiple choice or Pairings game option
* Start with the text filled in, certain words missing, you'd drag those in.
* Add other words to throw you off
