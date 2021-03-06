namespace py gene


struct hits_item {
  1: i32 entrezgene,
  2: string name,
  3: double _score,
  4: string symbol,
  5: string _id,
  6: i32 taxid,
}

struct cdk2{
  1:optional list<hits_item> hits,
  2:optional map<string,double> max_score,
  3:optional map<string,i32> took,
  4:optional map<string,i32> total,
}


/**
 * Ahh, now onto the cool part, defining a service. Services just need a name
 * and can optionally inherit from another service using the extends keyword.
 */
service Gene {

   cdk2 get()
}

/**
 * That just about covers the basics. Take a look in the test/ folder for more
 * detailed examples. After you run this file, your generated code shows up
 * in folders with names gen-<language>. The generated code isn't too scary
 * to look at. It even has pretty indentation.
 */
