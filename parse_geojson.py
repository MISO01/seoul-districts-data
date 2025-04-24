import geopandas as gpd
import pandas as pd

def main():
    # Shapefile 읽기 (인코딩 지정)
    gdf = gpd.read_file("emd_20230729/emd.shp", encoding="cp949")

    # 서울시 읍면동 정보 추출 (행정구역 코드가 "11"로 시작하는 데이터)
    seoul_emd = gdf[gdf["EMD_CD"].str.startswith("11", na=False)]

    # geometry 컬럼 제외하고 저장
    seoul_emd = seoul_emd.drop("geometry", axis=1)

    # CSV 파일로 저장
    seoul_emd.to_csv("seoul_emd_202307.csv", index=False, encoding="utf-8-sig")
    print(f"총 {len(seoul_emd)}개의 서울시 읍면동 정보를 추출했습니다.")

if __name__ == "__main__":
    main() 