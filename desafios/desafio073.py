# World Boxing Championship: https://box.live/world-rankings/wbc/?__cf_chl_captcha_tk__=f6a6d386a346ce1239eff68358cfa7aeb0f8d61f-1622616247-0-AUyBOdO6kSWj_2mSddzUEFrusSpp-s-u5Oxjl7_r0_9aqoIPdb5GpRnk933GEKF8Vlpe8eeZj-si2vx9awjAWBULWb-8GjvhboSN8ypsjL6v0nWfxWhdC6YzlFxolHX3PENgAR5MzlDJw2NSibBWNji_xFfWHmHpK7agrFAemfcuqgZBdh_mnerDHeUf-R09F9teBFDEl4N_Fkqm-fmaQ-mrqEzuk_9H9U53qljdRyPlpr7oOiOd3xH6W5u29TN1LUjHgT5T29nrcxHRRqVSZNVTACagA5iW-16Kf_UJIbZtlanxIfI_DfV8Va0dJGIhazV9Wm6m_WmVL-RNHgaBuumt1nF_9mlmnO-pE3_tZh4x54opkV3TjoFAAmbUf168e2PoSzh9RkMkwqbW6kV5eY_vOekgTXwoq4cjJTGftWYokOn0ezh0_EaOrTFPyErSUGJrXNfEXDWawTsxz9kO-bzHCwfaloAqrzlvejcBPfdNqW9v_71RSx2WrsKCzAfZYxK8KV9QBFYz4OJRn1gvXxTGUx_4089xa0tnFQy3g7_juYQV4AleQZy1kLC4sm_2Z1iRSkrNn2sGGyM86g5Jco2L0pOxK_ZQ-DK3uH7xaU7IVa-5L6Y8YGjGUmKXz7dZbqXU9rjak4i0V44ZLlrfYXEe7YCDjcgEZYUoRsUN2CFLyw5sD37v1itoQhu_F2laHQ
# 16 lutadores, em ordem decrescente no ranking.
FWei = ('Gary Russell Jr', 'Rey Vargas', 'Tugstsogt Nyambayar', 'Lerato Dlamini', 'Mauricio Lara', 'Mark Magsayo',
        'Kid Galahad', 'Josh Warrington', 'Joet Gonzalez', 'Hinata Maruta', 'Isaac Lowe', 'Julio Ceja',
        'Isaac Dogboe', 'Andoni Gago', 'Satoshi Shimizu', 'Dennis Contreras')
print(f'\033[33mOs primeiros cinco colocados são:\033[m\n{FWei[0:6]}')
print(f'Os últimos cinco colocados são:\n{FWei[-5:]}')
print(f'O ranking em ordem alfabética é:\n{sorted(FWei)}')
print(f'O Mark Magsayo está na {FWei.index("Mark Magsayo")}° posição.')
