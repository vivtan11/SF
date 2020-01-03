package com.vivek.xmlparse;

import static org.junit.Assert.assertEquals;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class XmlParseTest {

	@BeforeAll
	static void setUpBeforeClass() throws Exception {
	}

	@AfterAll
	static void tearDownAfterClass() throws Exception {
	}

	@BeforeEach
	void setUp() throws Exception {
	}

	@AfterEach
	void tearDown() throws Exception {
	}

	@Test
	void test() {
		// test proper XML input
		String testStr = "This is an abstract";
		assertEquals(null, XmlParse.getTextWithinTags("<abstract>"+testStr+"</abstract>"), testStr);
		
		// some other tag
		assertEquals(null, XmlParse.getTextWithinTags("<blah>"+testStr+"</blah>"), testStr);
		
		// badly formatted XML
		assertEquals(null, XmlParse.getTextWithinTags("<abstract>"+testStr+"</blah>"), "");
		assertEquals(null, XmlParse.getTextWithinTags(testStr), "");
		
		// I'd normally test for null & empty inputs, but we haven't added that code yet
	}

}
