﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MapAndSimulationChangeButton : MonoBehaviour {

    public MapXmlParser m_mapXmlParser;
    public SimulationXmlParser m_simXmlParser;

	// Use this for initialization
	void Start () {
		
	}

    string getPathFromType(AlgorithmChooser.AlgorithmType type)
    {
        string finalPath = "";
        string[] pathArray = MapChooser.mapPath.Split('/');
        string mapName = pathArray[pathArray.Length - 1];
        pathArray[pathArray.Length - 1] = mapName.Split('.')[0] + "_full_output.xml";
        foreach(string part in pathArray)
        {
            finalPath += part + '/';
        }
        return finalPath.Substring(0, finalPath.Length - 1);
    }

    public void onClick()
    {
        Debug.Log("poop");

        m_mapXmlParser.parseMap(MapChooser.mapPath);

        m_simXmlParser.parseSimulation(MapChooser.mapPath, getPathFromType(AlgorithmChooser.algorithmType));
    }
	
	// Update is called once per frame
	void Update () {
		
	}
}