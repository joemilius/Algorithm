function factorialize(num) {
    let product = 1
    while(num > 0){
      product = product * num
      num--
    }
    console.log(product);
  }

factorialize(5);
factorialize(10)
factorialize(20)
factorialize(0)