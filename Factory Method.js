function Computador(type, cpu, ram, hd) {
    this.type = type,
        this.cpu = cpu,
        this.ram = ram,
        this.hd = hd
}

Computador.prototype.toString = function () {
    return "Computador do tipo: " + this.type + ", Com CPU de: " + this.cpu + "Ghz," + " Hd de: " + this.hd + "Gb," + " e " + this.ram + "Gb de memoria Ram!";
};

var computador = new Computador('Sever', '2.1', '8', '900');
var computador2 = new Computador('PC', '3.5', '16', '120');
console.log(computador.toString());
console.log(computador2.toString());
