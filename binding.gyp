{
    'targets': [{
        'target_name':
        'node_ctp',
        'sources': [
            'src/addon.cc',
            'src/ctp_md.cc',
            'src/ctp_td.cc',
        ],
        'include_dirs': [
            '<(module_root_dir)/ctp_api/include',
        ],
        'conditions': [
            [
                'OS=="linux"',
                {
                    'cflags': ['-std=c++11'],
                    'libraries': [
                        '<(module_root_dir)/ctp_api/lib/linux64/libthostmduserapi.so',
                        '<(module_root_dir)/ctp_api/lib/linux64/libthosttraderapi.so',
                    ],
                    'include_dirs': [
                        '<(module_root_dir)/ctp_api/include',
                    ],
                }
            ],
            [
                "OS=='win'",
                {
                    "conditions": [
                        [
                            "target_arch=='ia32'",
                            {
                                "libraries":["<(module_root_dir)/ctp_api/lib/win32/thostmduserapi_se.lib", "<(module_root_dir)/ctp_api/lib/win32/thosttraderapi_se.lib"],
                                'include_dirs': [
                                    '<(module_root_dir)/ctp_api/include',
                                ],
                            },
                            { # target_arch=="x64"
                                "libraries":["<(module_root_dir)/ctp_api/lib/win64/thostmduserapi_se.lib", "<(module_root_dir)/ctp_api/lib/win64/thosttraderapi_se.lib"],
                                'include_dirs': [
                                    '<(module_root_dir)/ctp_api/include',
                                ],
                            }
                        ]
                    ]
                }
            ]
        ]
    }]
}
