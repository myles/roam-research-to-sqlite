# ruff: noqa: E501

BLOCK_ONE = {
    "string": "__Myles.Wiki__ is my public [[Commonplace Book]], it takes the contents of [[Wiki Sidebar]] and publishes them for others to see.",
    "create-time": 1646717989531,
    ":block/refs": [
        {":block/uid": "6e9iXvnoV"},
        {":block/uid": "c39lz3Efb"},
    ],
    "refs": [{"uid": "6e9iXvnoV"}, {"uid": "c39lz3Efb"}],
    ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
    "uid": "gtTLc0ifn",
    "edit-time": 1657387166779,
    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
}

BLOCK_TWO_CHILD_ONE = {
    "string": "[[Wiki Index]]",
    "create-time": 1657169767874,
    ":block/refs": [{":block/uid": "nzjaxAD5a"}],
    "refs": [{"uid": "nzjaxAD5a"}],
    ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
    "uid": "IQIM08TrH",
    "edit-time": 1657169782978,
    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
}

BLOCK_TWO_CHILD_TWO = {
    "string": "[[Wiki Sidebar]]",
    "create-time": 1657169758543,
    ":block/refs": [{":block/uid": "6e9iXvnoV"}],
    "refs": [{"uid": "6e9iXvnoV"}],
    ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
    "uid": "3YcNf6gjU",
    "edit-time": 1657169765079,
    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
}

BLOCK_TWO = {
    "string": "See Also",
    "create-time": 1657169749607,
    "heading": 1,
    ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
    "children": [BLOCK_TWO_CHILD_ONE, BLOCK_TWO_CHILD_TWO],
    "uid": "xOfOZ4-PR",
    "edit-time": 1657169758546,
    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
}

PAGE_ONE = {
    "create-time": 1639608343516,
    "title": "Myles.Wiki",
    ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
    "children": [
        BLOCK_ONE,
        BLOCK_TWO,
        {
            "string": "Metadata",
            "create-time": 1639608355402,
            "heading": 1,
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "children": [
                {
                    "string": "Website: [myles.wiki](https://myles.wiki/)",
                    "uid": "BQ377q_GU",
                    "create-time": 1639608355402,
                    "edit-time": 1639608362318,
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "Issue Tracking: N/A",
                    "uid": "ap8KnepnG",
                    "create-time": 1639608355402,
                    "edit-time": 1639608355402,
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "Built With: N/A",
                    "uid": "1wdOeoSNs",
                    "create-time": 1639608355402,
                    "edit-time": 1639608355402,
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
            ],
            "uid": "9wE1FuOLh",
            "edit-time": 1657169799620,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
    ],
    "uid": "q5bqSqK38",
    "edit-time": 1657169736551,
    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
}

PAGE_TWO = {
    "uid": "nzjaxAD5a",
    "create-time": 1657169782980,
    "edit-time": 1657169782981,
    "title": "Wiki Index",
    ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
}

PAGE_THREE = {
    "create-time": 1644432701189,
    "title": "Wiki Sidebar",
    ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
    "children": [
        {
            "string": "[[3D Printing]]",
            "create-time": 1657169618916,
            ":block/refs": [{":block/uid": "YI3dciILL"}],
            "refs": [{"uid": "YI3dciILL"}],
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "uid": "Y0jRMt2gl",
            "edit-time": 1657169688780,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "string": "[[Bullet Journal]]",
            "create-time": 1644433277717,
            ":block/refs": [{":block/uid": "mkvhQRpEL"}],
            "refs": [{"uid": "mkvhQRpEL"}],
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "uid": "hlNJ9wI3f",
            "edit-time": 1644433280697,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "string": "[[Data Science]]",
            "create-time": 1644433062791,
            ":block/refs": [{":block/uid": "5kG5nuOGs"}],
            "refs": [{"uid": "5kG5nuOGs"}],
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "uid": "XO44sCZK0",
            "edit-time": 1644433067325,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "edit-time": 1644432775328,
            "children": [
                {
                    "edit-time": 1646782902168,
                    "children": [
                        {
                            "string": "[[Adobe Fresco]]",
                            "create-time": 1646782902491,
                            ":block/refs": [{":block/uid": "GVhqrVnEH"}],
                            "refs": [{"uid": "GVhqrVnEH"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "TcASEk9Wy",
                            "edit-time": 1646782921071,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Adobe Illustrator]]",
                            "create-time": 1646782921420,
                            ":block/refs": [{":block/uid": "HDX-TGG_4"}],
                            "refs": [{"uid": "HDX-TGG_4"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "tVDx9jDvM",
                            "edit-time": 1646782935865,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Adobe InDesign]]",
                            "create-time": 1646782936134,
                            ":block/refs": [{":block/uid": "HfI0IQ7MP"}],
                            "refs": [{"uid": "HfI0IQ7MP"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "b25KHI5tB",
                            "edit-time": 1646782939739,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Adobe Lightroom]]",
                            "create-time": 1646782948634,
                            ":block/refs": [{":block/uid": "a6qa-ZqDr"}],
                            "refs": [{"uid": "a6qa-ZqDr"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "2IKbgXoif",
                            "edit-time": 1646782952795,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Adobe Photoshop]]",
                            "create-time": 1646782943015,
                            ":block/refs": [{":block/uid": "qlKmfNu1n"}],
                            "refs": [{"uid": "qlKmfNu1n"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "oh5Ghg3bZ",
                            "edit-time": 1646782947859,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Adobe Premiere]]",
                            "create-time": 1646782955476,
                            ":block/refs": [{":block/uid": "bXrSLu5M2"}],
                            "refs": [{"uid": "bXrSLu5M2"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "RhxvGeuH6",
                            "edit-time": 1646782963865,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                    ],
                    "refs": [{"uid": "UzmydXDPf"}],
                    "uid": "15VeLqAz2",
                    ":block/refs": [{":block/uid": "UzmydXDPf"}],
                    "string": "[[Adobe Creative Suite]]",
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "create-time": 1646782894744,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "Affinity",
                    "create-time": 1652732351279,
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "children": [
                        {
                            "string": "[[Affinity Designer]]",
                            "create-time": 1652732354363,
                            ":block/refs": [{":block/uid": "og0XXU4m7"}],
                            "refs": [{"uid": "og0XXU4m7"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "Yyh5M6JyC",
                            "edit-time": 1652732358070,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Affinity Photo]]",
                            "create-time": 1652732358063,
                            ":block/refs": [{":block/uid": "JviYMm2va"}],
                            "refs": [{"uid": "JviYMm2va"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "LxIWHamH4",
                            "edit-time": 1652732365919,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Affinity Publisher]]",
                            "create-time": 1652732365912,
                            ":block/refs": [{":block/uid": "6inh91zuW"}],
                            "refs": [{"uid": "6inh91zuW"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "qxs1438Hn",
                            "edit-time": 1652732368722,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                    ],
                    "uid": "tIBb5PqYX",
                    "edit-time": 1652732354369,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[Pen Plotters]]",
                    "create-time": 1644433082491,
                    ":block/refs": [{":block/uid": "2PGHxZnTm"}],
                    "refs": [{"uid": "2PGHxZnTm"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "5nkYcznVT",
                    "edit-time": 1644433093278,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[Zine]]",
                    "create-time": 1644433093257,
                    ":block/refs": [{":block/uid": "WIXJWYX6Y"}],
                    "refs": [{"uid": "WIXJWYX6Y"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "rFvK3_J2q",
                    "edit-time": 1644433103642,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
            ],
            "refs": [{"uid": "PqGJOSYJm"}],
            "uid": "r-FhDArpb",
            ":block/refs": [{":block/uid": "PqGJOSYJm"}],
            "string": "[[Graphic Design]]",
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "create-time": 1644432771701,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "edit-time": 1645981820969,
            "children": [
                {
                    "string": "[[Raspberry Pi]]",
                    "create-time": 1644432795405,
                    ":block/refs": [{":block/uid": "7izHsry5P"}],
                    "refs": [{"uid": "7izHsry5P"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "mjZ0kz9FY",
                    "edit-time": 1644432799411,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                }
            ],
            "refs": [{"uid": "q6WBD2LmT"}],
            "uid": "kUljAJwWc",
            ":block/refs": [{":block/uid": "q6WBD2LmT"}],
            "string": "[[Hardware]]",
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "create-time": 1644433126773,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "string": "[[IndieWeb]]",
            "create-time": 1657132863708,
            ":block/refs": [{":block/uid": "6FoTkpl2E"}],
            "refs": [{"uid": "6FoTkpl2E"}],
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "uid": "ba_dsUYfq",
            "edit-time": 1657132869139,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "edit-time": 1646717593752,
            "children": [
                {
                    "edit-time": 1646717598926,
                    "children": [
                        {
                            "string": "[[Reading list]]",
                            "create-time": 1646717633254,
                            ":block/refs": [{":block/uid": "_mOJOBOBW"}],
                            "refs": [{"uid": "_mOJOBOBW"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "Ns73vuS5U",
                            "edit-time": 1646717641274,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        }
                    ],
                    "refs": [{"uid": "9cPHf9sys"}],
                    "uid": "ilTapX4lv",
                    ":block/refs": [{":block/uid": "9cPHf9sys"}],
                    "string": "[[Books]]",
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "create-time": 1646717594042,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[Vinyl Library]]",
                    "create-time": 1646717604011,
                    ":block/refs": [{":block/uid": "bacsU9Bf8"}],
                    "refs": [{"uid": "bacsU9Bf8"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "RFP3ZFEpZ",
                    "edit-time": 1646717609903,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[Whisky Collection]]",
                    "create-time": 1646717610333,
                    ":block/refs": [{":block/uid": "TkBnlSaYz"}],
                    "refs": [{"uid": "TkBnlSaYz"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "npZm8kYHs",
                    "edit-time": 1646717625251,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
            ],
            "refs": [{"uid": "L2_5Jrkgl"}],
            "uid": "KYxaKBQug",
            ":block/refs": [{":block/uid": "L2_5Jrkgl"}],
            "string": "[[Libraries]]",
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "create-time": 1646717588560,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "edit-time": 1644432785853,
            "children": [
                {
                    "string": "[[Metasploit]]",
                    "create-time": 1644433024932,
                    ":block/refs": [{":block/uid": "G2lws4D_a"}],
                    "refs": [{"uid": "G2lws4D_a"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "kHi8Jsr0z",
                    "edit-time": 1644433027442,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[nmap]]",
                    "create-time": 1644433027431,
                    ":block/refs": [{":block/uid": "EA96SMLup"}],
                    "refs": [{"uid": "EA96SMLup"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "_5MX400eV",
                    "edit-time": 1644433031026,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
            ],
            "refs": [{"uid": "vuPaaAxzC"}],
            "uid": "PxU0N2WVj",
            ":block/refs": [{":block/uid": "vuPaaAxzC"}],
            "string": "[[Pentesting]]",
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "create-time": 1644432782890,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "edit-time": 1644789391492,
            "children": [
                {
                    "edit-time": 1644432737468,
                    "children": [
                        {
                            "string": "[[Fire OS]]",
                            "create-time": 1646268581936,
                            ":block/refs": [{":block/uid": "u7KxHLeQ9"}],
                            "refs": [{"uid": "u7KxHLeQ9"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "wV4Wz4mT6",
                            "edit-time": 1646268588926,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        }
                    ],
                    "refs": [{"uid": "QOK3ikJuU"}],
                    "uid": "wMWCy7x6X",
                    ":block/refs": [{":block/uid": "QOK3ikJuU"}],
                    "string": "[[Android]]",
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "create-time": 1644432730194,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[iOS]]",
                    "create-time": 1644432775406,
                    ":block/refs": [{":block/uid": "VUBYtCL1o"}],
                    "refs": [{"uid": "VUBYtCL1o"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "WkPwW0l5J",
                    "edit-time": 1644432779584,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[Linux]]",
                    "create-time": 1644432779578,
                    ":block/refs": [{":block/uid": "YcUQKwa6O"}],
                    "refs": [{"uid": "YcUQKwa6O"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "c3aLS_ATB",
                    "edit-time": 1644432782902,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[UNIX]]",
                    "create-time": 1644432806855,
                    ":block/refs": [{":block/uid": "UFNlS4TkF"}],
                    "refs": [{"uid": "UFNlS4TkF"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "iIoRqK9fm",
                    "edit-time": 1644432809368,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[Microsoft Windows]]",
                    "create-time": 1644432809338,
                    ":block/refs": [{":block/uid": "MPidEm7rd"}],
                    "refs": [{"uid": "MPidEm7rd"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "AEf65XGgD",
                    "edit-time": 1644432812636,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[macOS]]",
                    "create-time": 1644433481398,
                    ":block/refs": [{":block/uid": "Mn7jdGtGJ"}],
                    "refs": [{"uid": "Mn7jdGtGJ"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "O_at0jjOL",
                    "edit-time": 1644433485022,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
            ],
            "refs": [{"uid": "K7UvQBBZV"}],
            "uid": "tx0bx3Pb-",
            ":block/refs": [{":block/uid": "K7UvQBBZV"}],
            "string": "[[Operating Systems]]",
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "create-time": 1644432877998,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "string": "[[Photography]]",
            "create-time": 1644433337735,
            ":block/refs": [{":block/uid": "Zvu4uYhAd"}],
            "refs": [{"uid": "Zvu4uYhAd"}],
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "uid": "zaenHO2At",
            "edit-time": 1644433341306,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "edit-time": 1644432789155,
            "children": [
                {
                    "string": "[[Roam Research]]",
                    "create-time": 1647271830713,
                    ":block/refs": [{":block/uid": "KEKHfFS2q"}],
                    "refs": [{"uid": "KEKHfFS2q"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "_PHzEAHDz",
                    "edit-time": 1647271834974,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                }
            ],
            "refs": [{"uid": "hA1rwhQUn"}],
            "uid": "oD6Ae5yM4",
            ":block/refs": [{":block/uid": "hA1rwhQUn"}],
            "string": "[[Productivity]]",
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "create-time": 1644432785849,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "string": "[[Self-hosting]]",
            "create-time": 1644432799401,
            ":block/refs": [{":block/uid": "-1WkW8UUY"}],
            "refs": [{"uid": "-1WkW8UUY"}],
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "uid": "lOTHnGpy8",
            "edit-time": 1644433223429,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "edit-time": 1645981845731,
            "children": [
                {
                    "string": "[[Architectural Decision Records]]",
                    "create-time": 1647565413489,
                    ":block/refs": [{":block/uid": "M1mLM79lb"}],
                    "refs": [{"uid": "M1mLM79lb"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "rHHYsuX9Y",
                    "edit-time": 1647565416580,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "edit-time": 1644432747019,
                    "children": [
                        {
                            "string": "[[Artificial Intelligence]]",
                            "create-time": 1644432981736,
                            ":block/refs": [{":block/uid": "UZoiDeafh"}],
                            "refs": [{"uid": "UZoiDeafh"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "5THKdWOKA",
                            "edit-time": 1644432985701,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Machine Learning]]",
                            "create-time": 1644432985678,
                            ":block/refs": [{":block/uid": "tFYDcm3t6"}],
                            "refs": [{"uid": "tFYDcm3t6"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "4CCVSlylr",
                            "edit-time": 1644432988230,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                    ],
                    "refs": [{"uid": "OBxoHWZVx"}],
                    "uid": "-Em6cu5yv",
                    ":block/refs": [{":block/uid": "OBxoHWZVx"}],
                    "string": "[[Computer Science]]",
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "create-time": 1644432743627,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "edit-time": 1647271897672,
                    "children": [
                        {
                            "string": "[[Anaconda]]",
                            "create-time": 1647315734211,
                            ":block/refs": [{":block/uid": "SgY_rJd-l"}],
                            "refs": [{"uid": "SgY_rJd-l"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "C-G7fOaq4",
                            "edit-time": 1647315738549,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Jupyter Nootbook]]",
                            "create-time": 1647271897745,
                            ":block/refs": [{":block/uid": "oCPUnxXbo"}],
                            "refs": [{"uid": "oCPUnxXbo"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "IFft8BXnH",
                            "edit-time": 1647271900471,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Organizing Data Science Projects]]",
                            "create-time": 1647315926898,
                            ":block/refs": [{":block/uid": "EjgIzA-hU"}],
                            "refs": [{"uid": "EjgIzA-hU"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "J4sSoSgDd",
                            "edit-time": 1647315930355,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                    ],
                    "refs": [{"uid": "5kG5nuOGs"}],
                    "uid": "XmFRg7_Do",
                    ":block/refs": [{":block/uid": "5kG5nuOGs"}],
                    "string": "[[Data Science]]",
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "create-time": 1647271894152,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[Dat Protocol]]",
                    "create-time": 1644432747012,
                    ":block/refs": [{":block/uid": "lMifZwPGa"}],
                    "refs": [{"uid": "lMifZwPGa"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "LwjMOzRwD",
                    "edit-time": 1644432755125,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "edit-time": 1644432758176,
                    "children": [
                        {
                            "string": "[[Postgres]]",
                            "create-time": 1644433000950,
                            ":block/refs": [{":block/uid": "3cd2WjnsP"}],
                            "refs": [{"uid": "3cd2WjnsP"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "cBuILJFK3",
                            "edit-time": 1644433003266,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[MySQL]]",
                            "create-time": 1644433003252,
                            ":block/refs": [{":block/uid": "cEbNyQQLV"}],
                            "refs": [{"uid": "cEbNyQQLV"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "NBfGjxFTq",
                            "edit-time": 1644433005794,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                    ],
                    "refs": [{"uid": "yOcYp8wWL"}],
                    "uid": "c6nni4vWl",
                    ":block/refs": [{":block/uid": "yOcYp8wWL"}],
                    "string": "[[Database]]",
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "create-time": 1644432755115,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "edit-time": 1644432770979,
                    "children": [
                        {
                            "string": "[[Ansible]]",
                            "create-time": 1644433011213,
                            ":block/refs": [{":block/uid": "LH1MF8F24"}],
                            "refs": [{"uid": "LH1MF8F24"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "8IXD7AT-Q",
                            "edit-time": 1644433013385,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Docker]]",
                            "create-time": 1644433013374,
                            ":block/refs": [{":block/uid": "1SqNN8iH0"}],
                            "refs": [{"uid": "1SqNN8iH0"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "VaE983q-R",
                            "edit-time": 1644433016308,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                    ],
                    "refs": [{"uid": "zjNVKAp4D"}],
                    "uid": "-GuDpW-Lg",
                    ":block/refs": [{":block/uid": "zjNVKAp4D"}],
                    "string": "[[DevOps]]",
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "create-time": 1644432760024,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[JWT]]",
                    "create-time": 1648271543428,
                    ":block/refs": [{":block/uid": "6IdeCHZZi"}],
                    "refs": [{"uid": "6IdeCHZZi"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "W5YVgiACx",
                    "edit-time": 1648271547158,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "edit-time": 1644432792428,
                    "children": [
                        {
                            "string": "[[CSS]]",
                            "create-time": 1644433054754,
                            ":block/refs": [{":block/uid": "dDOb_Nrhx"}],
                            "refs": [{"uid": "dDOb_Nrhx"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "ONsmIxkBH",
                            "edit-time": 1644433054754,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Go]]",
                            "create-time": 1644433054754,
                            ":block/refs": [{":block/uid": "mHM_vqGuk"}],
                            "refs": [{"uid": "mHM_vqGuk"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "P8YBIUovS",
                            "edit-time": 1644433054754,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[HTML]]",
                            "create-time": 1646782873226,
                            ":block/refs": [{":block/uid": "vhy4RPBO4"}],
                            "refs": [{"uid": "vhy4RPBO4"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "kXAZf07c8",
                            "edit-time": 1646782876771,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "edit-time": 1644433054754,
                            "children": [
                                {
                                    "string": "[[npm]]",
                                    "create-time": 1646091165968,
                                    ":block/refs": [
                                        {":block/uid": "Nc1Xy8TKe"}
                                    ],
                                    "refs": [{"uid": "Nc1Xy8TKe"}],
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "uid": "FfuoyZKif",
                                    "edit-time": 1646091172383,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                },
                                {
                                    "string": "[[Node.js]]",
                                    "create-time": 1646091216930,
                                    ":block/refs": [
                                        {":block/uid": "ogKOGGPxp"}
                                    ],
                                    "refs": [{"uid": "ogKOGGPxp"}],
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "uid": "pHIql776R",
                                    "edit-time": 1646091223013,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                },
                                {
                                    "string": "[[Vite]]",
                                    "create-time": 1647116801215,
                                    ":block/refs": [
                                        {":block/uid": "jbyAUeuu_"}
                                    ],
                                    "refs": [{"uid": "jbyAUeuu_"}],
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "uid": "jOwBa4Av_",
                                    "edit-time": 1647116805031,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                },
                                {
                                    "edit-time": 1646091184591,
                                    "children": [
                                        {
                                            "string": "[[Nuxt.js]]",
                                            "create-time": 1646091172765,
                                            ":block/refs": [
                                                {":block/uid": "wJwhbf8bc"}
                                            ],
                                            "refs": [{"uid": "wJwhbf8bc"}],
                                            ":create/user": {
                                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                            },
                                            "uid": "c7UXeDtDl",
                                            "edit-time": 1646091176771,
                                            ":edit/user": {
                                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                            },
                                        },
                                        {
                                            "string": "[[VuePress]]",
                                            "create-time": 1646091188875,
                                            ":block/refs": [
                                                {":block/uid": "gdoCc4kJm"}
                                            ],
                                            "refs": [{"uid": "gdoCc4kJm"}],
                                            ":create/user": {
                                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                            },
                                            "uid": "sHK95DMdv",
                                            "edit-time": 1646091192933,
                                            ":edit/user": {
                                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                            },
                                        },
                                    ],
                                    "refs": [{"uid": "mq75Hiakx"}],
                                    "uid": "t6OrUacLA",
                                    ":block/refs": [
                                        {":block/uid": "mq75Hiakx"}
                                    ],
                                    "string": "[[Vue.js]]",
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "create-time": 1646091180937,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                },
                                {
                                    "edit-time": 1646091237240,
                                    "children": [
                                        {
                                            "string": "[[React Native]]",
                                            "create-time": 1646091237231,
                                            ":block/refs": [
                                                {":block/uid": "XgXjUd1St"}
                                            ],
                                            "refs": [{"uid": "XgXjUd1St"}],
                                            ":create/user": {
                                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                            },
                                            "uid": "rXEVMPC0j",
                                            "edit-time": 1646091243088,
                                            ":edit/user": {
                                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                            },
                                        },
                                        {
                                            "string": "[[React Navigation]]",
                                            "create-time": 1646091243238,
                                            ":block/refs": [
                                                {":block/uid": "WYFj0ZbD7"}
                                            ],
                                            "refs": [{"uid": "WYFj0ZbD7"}],
                                            ":create/user": {
                                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                            },
                                            "uid": "mGyJciAVz",
                                            "edit-time": 1646091258963,
                                            ":edit/user": {
                                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                            },
                                        },
                                    ],
                                    "refs": [{"uid": "FY48yf3Vl"}],
                                    "uid": "B2hCphpgE",
                                    ":block/refs": [
                                        {":block/uid": "FY48yf3Vl"}
                                    ],
                                    "string": "[[React]]",
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "create-time": 1646091224957,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                },
                            ],
                            "refs": [{"uid": "gkcGwMylg"}],
                            "uid": "Rsiqo83xr",
                            ":block/refs": [{":block/uid": "gkcGwMylg"}],
                            "string": "[[JavaScript]]",
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "create-time": 1644433054754,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Julia]]",
                            "create-time": 1646333496601,
                            ":block/refs": [{":block/uid": "kHaYt9t1r"}],
                            "refs": [{"uid": "kHaYt9t1r"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "S_DuDcMTb",
                            "edit-time": 1646333500863,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "edit-time": 1644433054754,
                            "children": [
                                {
                                    "string": "[[Laravel]]",
                                    "create-time": 1647315865004,
                                    ":block/refs": [
                                        {":block/uid": "75HAp1kQF"}
                                    ],
                                    "refs": [{"uid": "75HAp1kQF"}],
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "uid": "FqTvgx8M0",
                                    "edit-time": 1647315869822,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                },
                                {
                                    "string": "[[WordPress]]",
                                    "create-time": 1647315856051,
                                    ":block/refs": [
                                        {":block/uid": "QhZYD4c4e"}
                                    ],
                                    "refs": [{"uid": "QhZYD4c4e"}],
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "uid": "zAL92pd9n",
                                    "edit-time": 1647315862075,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                },
                            ],
                            "refs": [{"uid": "6uIF6R8XE"}],
                            "uid": "QGRUbXxhf",
                            ":block/refs": [{":block/uid": "6uIF6R8XE"}],
                            "string": "[[PHP]]",
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "create-time": 1644433054754,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "edit-time": 1644433054754,
                            "children": [
                                {
                                    "string": "[[Celery]]",
                                    "create-time": 1647315845717,
                                    ":block/refs": [
                                        {":block/uid": "xcIpdbU7f"}
                                    ],
                                    "refs": [{"uid": "xcIpdbU7f"}],
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "uid": "Ttkjf78JU",
                                    "edit-time": 1647315849268,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                },
                                {
                                    "edit-time": 1647315842171,
                                    "children": [
                                        {
                                            "string": "[[Wagtail]]",
                                            "create-time": 1647315886928,
                                            ":block/refs": [
                                                {":block/uid": "VnZtNf69i"}
                                            ],
                                            "refs": [{"uid": "VnZtNf69i"}],
                                            ":create/user": {
                                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                            },
                                            "uid": "rv1pmIRKn",
                                            "edit-time": 1647315891445,
                                            ":edit/user": {
                                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                            },
                                        }
                                    ],
                                    "refs": [{"uid": "_HId7v3pJ"}],
                                    "uid": "_PfdiM97x",
                                    ":block/refs": [
                                        {":block/uid": "_HId7v3pJ"}
                                    ],
                                    "string": "[[Django]]",
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "create-time": 1647315838274,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                },
                                {
                                    "string": "[[lazy-myles]]",
                                    "create-time": 1647315876037,
                                    ":block/refs": [
                                        {":block/uid": "Nvl1jHkzA"}
                                    ],
                                    "refs": [{"uid": "Nvl1jHkzA"}],
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "uid": "uYGmP-yME",
                                    "edit-time": 1647315879715,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                },
                                {
                                    "string": "[[Pandas]]",
                                    "create-time": 1646101354087,
                                    ":block/refs": [
                                        {":block/uid": "ZIuioCG0c"}
                                    ],
                                    "refs": [{"uid": "ZIuioCG0c"}],
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "uid": "SMjZ16Mlv",
                                    "edit-time": 1646101359908,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                },
                                {
                                    "string": "[[Collection Python Regular Expression]]",
                                    "create-time": 1647316279246,
                                    ":block/refs": [
                                        {":block/uid": "UVu6JLLYa"}
                                    ],
                                    "refs": [{"uid": "UVu6JLLYa"}],
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "uid": "ZLV17j6KP",
                                    "edit-time": 1647316298209,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                },
                            ],
                            "refs": [{"uid": "8ot9-9Kx5"}],
                            "uid": "hXqBkCM3A",
                            ":block/refs": [{":block/uid": "8ot9-9Kx5"}],
                            "string": "[[Python]]",
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "create-time": 1644433054754,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[R]]",
                            "create-time": 1644433495679,
                            ":block/refs": [{":block/uid": "UZrDwoP3Q"}],
                            "refs": [{"uid": "UZrDwoP3Q"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "GVDAe2nNr",
                            "edit-time": 1644433497957,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "edit-time": 1644433054754,
                            "children": [
                                {
                                    "edit-time": 1646269101135,
                                    "children": [
                                        {
                                            "string": "[[Jekyll::Typogrify]]",
                                            "create-time": 1646269101425,
                                            ":block/refs": [
                                                {":block/uid": "gGVkEXxSo"}
                                            ],
                                            "refs": [{"uid": "gGVkEXxSo"}],
                                            ":create/user": {
                                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                            },
                                            "uid": "Gne25HgE0",
                                            "edit-time": 1646269105676,
                                            ":edit/user": {
                                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                            },
                                        }
                                    ],
                                    "refs": [{"uid": "eV2wneTZj"}],
                                    "uid": "BF0zQr-7Q",
                                    ":block/refs": [
                                        {":block/uid": "eV2wneTZj"}
                                    ],
                                    "string": "[[Jekyll]]",
                                    ":create/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                    "create-time": 1646269097061,
                                    ":edit/user": {
                                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                                    },
                                }
                            ],
                            "refs": [{"uid": "zjGkGq9Wj"}],
                            "uid": "d1shZ2BQp",
                            ":block/refs": [{":block/uid": "zjGkGq9Wj"}],
                            "string": "[[Ruby]]",
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "create-time": 1644433054754,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                        {
                            "string": "[[Rust]]",
                            "create-time": 1644433054754,
                            ":block/refs": [{":block/uid": "g-SUEPGKG"}],
                            "refs": [{"uid": "g-SUEPGKG"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "rkabGFXK_",
                            "edit-time": 1644433054754,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        },
                    ],
                    "refs": [{"uid": "TQf9nsAbf"}],
                    "uid": "g6PKQnD1C",
                    ":block/refs": [{":block/uid": "TQf9nsAbf"}],
                    "string": "[[Programming]]",
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "create-time": 1644432789091,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "edit-time": 1644432806869,
                    "children": [
                        {
                            "string": "[[Visual Studio Code]]",
                            "create-time": 1647271851742,
                            ":block/refs": [{":block/uid": "zUmx3Bsju"}],
                            "refs": [{"uid": "zUmx3Bsju"}],
                            ":create/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                            "uid": "1x8CWKoHp",
                            "edit-time": 1647271855041,
                            ":edit/user": {
                                ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                            },
                        }
                    ],
                    "refs": [{"uid": "H-R1K0B5X"}],
                    "uid": "hZnakWf1E",
                    ":block/refs": [{":block/uid": "H-R1K0B5X"}],
                    "string": "[[Text Editors]]",
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "create-time": 1644432802321,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
            ],
            "refs": [{"uid": "JF-frD-iy"}],
            "uid": "kws-Kxyq-",
            ":block/refs": [{":block/uid": "JF-frD-iy"}],
            "string": "[[Software Engineering]]",
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "create-time": 1644432831941,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "string": "[[Startups]]",
            "create-time": 1647316000453,
            ":block/refs": [{":block/uid": "oWgdL2uuW"}],
            "refs": [{"uid": "oWgdL2uuW"}],
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "uid": "Ws_VgXnJK",
            "edit-time": 1647316011653,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "string": "[[Tarot Cards]]",
            "create-time": 1647315967759,
            ":block/refs": [{":block/uid": "Av41kE9HH"}],
            "refs": [{"uid": "Av41kE9HH"}],
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "uid": "M8PzK2yhc",
            "edit-time": 1647315975904,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
        {
            "edit-time": 1644433179792,
            "children": [
                {
                    "string": "[[Difference between UI and UX]]",
                    "create-time": 1644433180919,
                    ":block/refs": [{":block/uid": "jZLIJqVHr"}],
                    "refs": [{"uid": "jZLIJqVHr"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "zPIZZrIca",
                    "edit-time": 1644433185515,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
                {
                    "string": "[[Information Architecture]]",
                    "create-time": 1645981766812,
                    ":block/refs": [{":block/uid": "mXOo0Z3W9"}],
                    "refs": [{"uid": "mXOo0Z3W9"}],
                    ":create/user": {
                        ":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"
                    },
                    "uid": "je4zGX58T",
                    "edit-time": 1645981779036,
                    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
                },
            ],
            "refs": [{"uid": "d-yopZoa4"}, {"uid": "3rWj0RNsu"}],
            "uid": "Oiz4RkjnJ",
            ":block/refs": [
                {":block/uid": "d-yopZoa4"},
                {":block/uid": "3rWj0RNsu"},
            ],
            "string": "[[User Interface]] & [[User Experience]]",
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            "create-time": 1644433168538,
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        },
    ],
    "uid": "6e9iXvnoV",
    "edit-time": 1644433408966,
    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
}

DAILY_NOTE_PAGE = {
    "create-time": 1684196441818,
    "title": "May 15th, 2023",
    ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
    ":log/id": 1684196441817,
    "children": [
        {
            "string": "Hello, World!",
            "uid": "8oIBZ4uNW",
            "create-time": 1684196447241,
            "edit-time": 1684196451610,
            ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
            ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
        }
    ],
    "uid": "05-15-2023",
    "edit-time": 1684196441818,
    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
}

USER_PAGE = {
    "uid": "B-ltsPPpS",
    "create-time": 1684196441809,
    "edit-time": 1684196441809,
    "title": "Anonymous",
    ":create/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
    ":edit/user": {":user/uid": "dVUi6J6XIea0FheVrBJjChtcOID2"},
}

PAGES = [PAGE_ONE, PAGE_TWO, PAGE_THREE]
