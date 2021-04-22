export interface XmlElement {
  name: string;
  type: string;
  minOccurs?: number | "unbounded";
  maxOccurs?: number | "unbounded";
}

export interface XmlComplexType {
  name: string;
  sequence: {
    element: XmlElement | XmlElement[];
    choice?: XmlElement[] | XmlElement;
    minOccurs?: number | "unbounded";
    maxOccurs?: number | "unbounded";
  };
  choice?: {
    element: XmlElement | XmlElement[];
    minOccurs?: number | "unbounded";
    maxOccurs?: number | "unbounded";
  };
}

export type XmlComplexTypes = XmlComplexType[];
export interface RootState {
  complexTypeData: XmlComplexTypes;
  xmlFile: string;
  isConnected: boolean;
  socketMessage: string;
}
