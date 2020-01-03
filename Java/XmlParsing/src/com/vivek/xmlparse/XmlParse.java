package com.vivek.xmlparse;

import java.io.*;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.xml.sax.InputSource;

public class XmlParse {
	
	// Given an XML element <abstract>text</abstract>, returns text. If the input XML cannot 
	// be parsed for whatever reason, an empty string ("") is returned. 
	// An easy way is to extract the substring between <abstract> and </abstract> using
	// Java string functionality. This is fast.  
	// A more generic way is to parse the XML using a DOM parser (the XML is small, and DOM's 
	// easier to code than SAX). While perhaps an overkill for wiki abstracts, it can be used
	// later for other kinds of tags, or more complex XML. 
	public static String getTextWithinTags(String inputXML) {
        DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
        DocumentBuilder db = null;
        try {
            db = dbf.newDocumentBuilder();
            InputSource is = new InputSource();
            is.setCharacterStream(new StringReader(inputXML));
        	// parse the XML
            Document doc = db.parse(is);
            // extract the root element's text
            return (doc.getDocumentElement().getTextContent());
        } 
        // ideally, catch SAXParseException or similar parsing exceptions
        catch (Exception e1) {
        	e1.printStackTrace();
        }
        // we could also just thrown an exception instead of returning an empty string
        return "";
	}

	// I've hard-coded the input and output files for ease of use, but they would ideally 
	// be passed as arguments to the program
	public static void main(String[] args) {

		// The input XML file can be extremely large. One method to get all abstracts is to 
		// read the file as a whole, parse it as an XML doc, then extract 'abstract' elements. 
		// But the input file size can cause issues with parsing the whole file. 
		// Instead, we read each line, process any line with the '<abstract>' tab, and ignore the
		// rest. Less generic, but much better performance with large files. 
		try (BufferedReader br = new BufferedReader(new FileReader("wiki-abstract.xml"));
				PrintWriter pw = new PrintWriter(new FileWriter("wiki-abstracts-only.txt"));) {
			String line;
			// read each line & process
			while ((line = br.readLine()) != null) {
				// search for lines starting with <abstract> and whose text doesn't start with '|', as
				// these are not usable abstracts
	            if ((line.startsWith("<abstract>")) && !(line.startsWith("<abstract>|"))) {
	            	String res = XmlParse.getTextWithinTags(line);
	            	if (!res.isEmpty()) {
	            		pw.println(res);
	            	}
	            }
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		System.out.println("Finished processing");
	}

}
