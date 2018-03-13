class Feature {
  constructor(opt) {
    this.id = null;
    this.title = null;
    this.description = null;
    this.client = null;
    this.priority = null;
    this.target_date = null;
    this.product_area = null;

    this.merge_parameters(opt);
  }

  merge_parameters(opts) {
    for (var i in opts) {
      if (this.hasOwnProperty(i)) {
        this[i] = opts[i];
      }
    }
  }
}

export default Feature;
