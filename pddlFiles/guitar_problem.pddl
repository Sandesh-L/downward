(define (problem music_piece)
  (:domain guitar_fretboard)
  (:objects
    noteF4 noteG4 noteE4 noteE5 noteB4 noteA4 noteC5 noteD5 noteF5 noteG5 noteA5 - note
    loc0_1 loc1_6 loc2_15 loc3_10 loc0_3 loc1_8 loc2_17 loc3_12 loc0_0 loc1_5 loc2_14 loc3_9
    loc0_12 loc1_17 loc0_7 loc1_12 loc3_16 loc0_5 loc1_10 loc3_14 loc0_8 loc1_13 loc3_17 loc0_10 loc1_15
    loc0_13 loc1_18 loc0_15 loc0_17 - location
  )
  (:init
    ; Note to location matches
    (matches loc0_1 noteF4) (matches loc1_6 noteF4) ; And so on for each note-location pair
    ; Initial note placements
    ; This section will be empty initially as no notes are placed yet.
  )
  (:goal
    (and
      (note-placed noteF4) (note-placed noteG4) ; And so on for each note
    )
  )
)
