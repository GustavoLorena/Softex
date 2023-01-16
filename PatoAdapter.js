class Pato {  
    speak() {
      console.log(' Quack Quack');
    }
  }
  
  class AdaptadorPato extends Pato {
    speak() {
      console.log('Cocorico');
    }
  }

  class AdaptadorPatoDemo extends Pato {
    speak() {
        console.log('QuaQuaQua');
    }
  }
  

  var Galinha = new AdaptadorPatoDemo();
  var Pato1 = new AdaptadorPato();
  Galinha.speak();
  Pato1.speak();
