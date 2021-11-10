function bouncer(arr) {
    //  let truthy = [] 
    //   for(let i = 0; i < arr.length; i++){
    //       if(arr[i]){
    //         truthy.push(arr[i])
    //       }
    //   }
    //  console.log(truthy)
      console.log (arr.filter(Boolean));
    }
        
    
    bouncer([7, "ate", "", false, 9]);
    bouncer([false, null, 0, NaN, undefined, ""])
    bouncer(["a", "b", "c"]) 