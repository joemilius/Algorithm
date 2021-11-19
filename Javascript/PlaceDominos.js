function placeDominos(L,D,A){
    let currentLayout = []
    let minMoves = -1
    let newDistance
  
    for (let i = 0; i <= L; i += D){
      currentLayout.push(i)
    }
    for (let i = 0; i <= A.length - 1; i++){
      let moves = 0
      let possibleLayout = []
      for (let j = 0; j <= L; j += A[i]){
        possibleLayout.push(j)
      }
      for (let j = 0; j < currentLayout.length; j++){
        if (!possibleLayout.includes(currentLayout[j])){
          moves++
        }
      }
      for (let j = 0; j < possibleLayout.length; j++){
        if (!currentLayout.includes(possibleLayout[j])){
          moves++
        }
      }
      if (minMoves > moves || minMoves === -1){
        minMoves = moves
        newDistance = A[i]
      }
    }
    return newDistance
  }

/*
You are in the finals of a national domino-placing competition. Unfortunately, the loud crowd prevented you from 
hearing the judge’s full instructions. All you were able to catch is that you need to evenly place your dominos in a 
straight line of maximum length L. 
 
After you finish placing each of your dominos D distance apart, the judge tells you that your arrangement is invalid! 
Instead of spacing your dominos D distance apart, you were supposed to space them by one of the distances 
provided in array A instead. 
 
You realize that you can still salvage the situation - depending on which new distance you choose, some of the 
dominos that you previously placed can still be used in your final arrangement. However, keep in mind that every 
domino that you pick up or put down can potentially knock over your other dominos so you want to limit moving 
too many of them around. 
 
Write a function placeDominos() that will accept 3 arguments: 
 
L – maximum length of your line of dominos (integer) 
D – original distance between dominos (integer) 
A – list of possible new distances (array of integers) 
 
Your function should return the new distance that you should choose in order to update your invalid domino 
arrangement into a valid arrangement in the fewest possible moves (Note: A move consists of either picking up a 
domino or putting down a domino). 
  
Example: 
L = 100, D = 25, A = [15, 50] 
 
The original dominos are placed 25 distance apart at 0, 25, 50, 75, 100 
 
Choosing a new distance of 15 needs dominos at 0, 15, 30, 45, 60, 75, 90 
- This requires 8 total moves (3 pick-ups and 5 put-downs) 
 
Choosing a new distance of 50 needs dominos at 0, 50, 100 
- This requires 2 total moves (2 pick-ups) 
 
Your function should return 50, because changing to that distance requires 
the fewest number of moves (2 total moves – pick up the dominos at 25 and 75)
*/