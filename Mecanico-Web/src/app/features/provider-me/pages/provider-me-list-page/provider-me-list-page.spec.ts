import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ProviderMeListPage } from "./provider-me-list-page";

describe("ProviderMeListPage", () => {
	let component: ProviderMeListPage;
	let fixture: ComponentFixture<ProviderMeListPage>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ProviderMeListPage],
		}).compileComponents();

		fixture = TestBed.createComponent(ProviderMeListPage);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
