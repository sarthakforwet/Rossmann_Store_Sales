function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.store = values[0];
    obj.dayofweek = values[1];
    obj.date = values[2];
    obj.sales = values[3];
    obj.customers = values[4];
    obj.open = values[5];
    obj.promo = values[6];
    obj.stateholiday = values[7];
    obj.schoolholiday = values[8];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }