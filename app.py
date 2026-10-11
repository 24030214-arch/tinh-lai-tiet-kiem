<meta charset="utf-8">
<h2>Tính lãi gửi tiết kiệm</h2>

Số tiền gửi: <input id="tien" type="number"><br>
Số tháng: <input id="thang" type="number"><br>
Lãi suất %/năm: <input id="lai" type="number"><br>

<select id="loai">
  <option value="don">Lãi đơn</option>
  <option value="kep">Lãi kép</option>
</select>

<button onclick="tinh()">Tính</button>
<p id="kq"></p>
