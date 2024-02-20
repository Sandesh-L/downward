(define (domain guitar_fretboard)
  (:requirements :strips :typing)
  (:types location note)
  (:predicates
    (matches ?l - location ?n - note)
    (note-placed ?n - note)
  )

    (:action place-note
    :parameters (?n - note ?l - location)
    :precondition (and (matches ?l ?n))
    :effect (and (note-placed ?n))
)
)
