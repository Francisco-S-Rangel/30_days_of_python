from dataclasses import dataclass
from typing import Optional

@dataclass
class Box:
    id: Optional[int] = None
    key: Optional[bool] = None
    child: Optional['Box'] = None

boxes = Box(
    id=1,
    child=Box(
        id=2,
        child=Box(
            id=3,
            child=Box(
                id=4,
                child=Box(
                    id=5,
                    key=True
                )
            )
        )
    )
)

boxes_two = Box(
    id=1,
    child=Box(
        id=2,
        child=Box(
            id=3,
            child=Box(
                id=4,
                child=Box(
                    id=5
                )
            )
        )
    )
)

def search_for_the_key(box: Box) -> bool:
    if box.key:
        print(f"The key is in the box - id: {box.id}")
        return True
    
    if box.child:
        return search_for_the_key(box.child)

    return False

if not search_for_the_key(boxes):
    print("The key was not found!")

if not search_for_the_key(boxes_two):
    print("The key was not found!")